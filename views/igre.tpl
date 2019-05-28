% rebase('Repozitorij/vislice/views/base.tpl')
% import model

<table>
  <tr>
    <td><h3>{{ id_igre }}</h3></td>
  </tr>
  <tr>
    <td><h3>{{ igra.pravilni_del_gesla() }}</h3></td>
  </tr>
  <tr>
    <td>Neuspeli poskusi:</td>
    <td>{{ igra.nepravilni_ugibi() }}</td>
  </tr>

  % if poskus == model.ZMAGA or poskus == model.PORAZ:
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % else:
  <tr>
      <td bgcolor="blue">
        <form action="/igra/" method="post">
          <input type="text" name="poskus">
          <input type="submit" value="Ugibaj">
        </form>
      </td>
  </tr>
  % end
</table>